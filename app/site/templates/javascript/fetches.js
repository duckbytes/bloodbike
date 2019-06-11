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

function make_fetch(url, type, auth, content_type = undefined, data = undefined) {
    console.error(url, type, auth, content_type, data);
    return fetch("{{ api_url }}" + url, {
        method: type,
        withCredentials: true,
        credentials: 'include',
        headers: new Headers({
            'Authorization': auth,
            'Content-type': content_type ? content_type :  "text/html"
        }),
        body: data ? JSON.stringify(data) : undefined
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

class Vehicle {
    constructor(bearer){
        this.bearer = bearer;
    }

    async get_vehicles(user_id) {
        let self = this;
        return make_fetch("vehicles/" + user_id, "GET", self.bearer)
    }

    async get_vehicle(vehicle_id) {
        let self = this;
        return make_fetch("vehicle/" + vehicle_id, "GET", self.bearer)
    }

    async create_vehicle(input_data) {
        let self = this;
        return make_fetch("vehicles", "POST", self.bearer, "application/json", input_data)
    }
}

class Note {
    constructor(bearer){
        this.bearer = bearer;
    }

    async get_notes(item_id) {
        let self = this;
        return make_fetch("notes/" + item_id, "GET", self.bearer)
    }

    async get_note(note_id) {
        let self = this;
        return make_fetch("note/" + note_id, "GET", self.bearer)
    }

    async create_note(input_data) {
        let self = this;
        return make_fetch("notes", "POST", self.bearer, "application/json", input_data)
    }
}

class Task {
    constructor(bearer){
        this.bearer = bearer;
    }

    async get_tasks(session_id) {
        let self = this;
        return make_fetch("tasks" + session_id, "GET", self.bearer)
    }

    async get_task(task_id) {
        let self = this;
        return make_fetch("task/" + task_id, "GET", self.bearer)
    }

    async create_task(input_data) {
        let self = this;
        return make_fetch("tasks", "POST", self.bearer, "application/json", input_data)
    }
}

class Session {
    constructor(bearer){
        this.bearer = bearer;
        this.users = undefined;
    }

    async get_sessions(user_id) {
        let self = this;
        return make_fetch("sessions/" + user_id, "GET", self.bearer)
    }

    async get_session(session_id) {
        let self = this;
        return make_fetch("session/" + session_id, "GET", self.bearer)

    }

    async create_session(input_data) {
        let self = this;
        if (input_data) {
            return make_fetch("sessions", "POST", self.bearer, "application/json", input_data)
        }
        else  {
            return make_fetch("sessions", "POST", self.bearer)
        }
    }

}

class User {
    constructor(bearer){
        this.bearer = bearer;
        this.users = undefined;
    }

    async get_users() {
        let self = this;
        return make_fetch("users", "GET", self.bearer)
    }

    async get_user(user_id) {
        let self = this;
        return make_fetch("user/" + user_id, "GET", self.bearer)

    }

    async create_user(input_data) {
        let self = this;
        return make_fetch("users", "POST", self.bearer, "application/json", input_data)
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
                self.sessions = new Session(self.bearer);
                self.notes = new Note(self.bearer);
                self.tasks = new Task(self.bearer);
                self.vehicles = new Vehicle(self.bearer);
                self.initialised = true;
            })
            .catch(function (error) {
                console.log("Request failed", error);
                return data;
            });
    }
}
