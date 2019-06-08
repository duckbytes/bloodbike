const fetch = require('node-fetch');
global.Headers = fetch.Headers;


function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject(new Error(response.statusText))
    }
}

function json(response) {
    return response.json()
}


class users {

    constructor(){
        this.token = "";
        this.bearer = "";
    }

    login(username, password) {
        let self = this;
        fetch('http://localhost:5000/api/v0.1/login', {
            method: 'post',
            headers: {
                "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: 'username=' + username + '&password=' + password
        })
            .then(json)
            .then(function (data) {
                console.log('Request succeeded with JSON response', data);
                self.token = data['access_token'];
                self.bearer = "Bearer " + self.token;
            })
            .catch(function (error) {
                console.log('Request failed', error);
            });

    }

    get_users() {
        let self = this;
        fetch('http://localhost:5000/api/v0.1/users', {
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
            }).catch(function (error) {
            console.log('Request failed', error);
        });
    }

    get_user(user_id) {
        let self = this;
        fetch('http://localhost:5000/api/v0.1/user/' + user_id, {
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
            }).catch(function (error) {
            console.log('Request failed', error);
        });

    }

    create_user(data) {
        let self = this;
        fetch('http://localhost:5000/api/v0.1/users', {
            method: 'POST',
            withCredentials: true,
            credentials: 'include',
            headers: new Headers({
                'Authorization': self.bearer,
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify(data)
        })
            .then(json)
            .then(function (data) {
                console.log('Request succeeded with JSON response', data);
            })
            .catch(function (error) {
                console.log('Request failed', error);
            });

    }
}

module.exports = {
    users
};
