function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject({ "status_code": response.status, "error": new Error(response.statusText), "response": response.json() })
    }
}

function json(response) {
    return response.json()
}

class User {
    constructor(bearer){
        this.bearer = bearer;
        this.users = undefined;
    }

    async get_users() {
        let self = this;
        return fetch("{{ api_url }}users", {
            method: 'GET',
            withCredentials: true,
            credentials: 'include',
            headers: new Headers({
                'Authorization': self.bearer,
                'Content-Type': 'application/json'
            })
        })
            .then(status)
            .then(json)
            .then(function (data) {
                console.log('Request succeeded with JSON response', data);
                self.users = data;
                return data;
            }).catch(function (error) {
                console.log('Request failed', error);
                return data;
        });
    }

    async get_user(user_id) {
        let self = this;
        return fetch('{{api_url}}user/' + user_id, {
            method: 'GET',
            withCredentials: true,
            credentials: 'include',
            headers: new Headers({
                'Authorization': self.bearer,
                'Content-Type': 'application/json'
            })
        })
            .then(status)
            .then(json)
            .then(function (data) {
                console.log('Request succeeded with JSON response', data);
                return data;
            }).catch(function (error) {
                console.log('Request failed', error);
                return data;
        });

    }

    async create_user(input_data) {
        let self = this;
        return fetch('{{api_url}}users', {
            method: 'POST',
            withCredentials: true,
            credentials: 'include',
            headers: new Headers({
                'Authorization': self.bearer,
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify(input_data)
        })
            .then(status)
            .then(json)
            .then(function (data) {
                console.log('Request succeeded with JSON response', data);
                return data;
            })
            .catch(function (data) {
                console.log('Request failed', data['error'], data['status_code']);
                return data['response'];
            });

    }
}

class Control {
    constructor(){
        this.token = "";
        this.bearer = "";
        this.initialised = false;
        this.users = undefined;
    }

    async login(username, password) {
        let self = this;
        fetch('{{api_url}}login', {
            method: 'post',
            headers: {
                "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: 'username=' + username + '&password=' + password
        })
            .then(status)
            .then(json)
            .then(function (data) {
                console.log("Login successful");
                self.token = data['access_token'];
                self.bearer = "Bearer " + self.token;
                self.users = new User(self.bearer);
                self.initialised = true;
            })
            .catch(function (error) {
                console.log("Request failed", error);
                return data;
            });
    }
}
