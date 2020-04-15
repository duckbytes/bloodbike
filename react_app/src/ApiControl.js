import { store } from 'react-notifications-component';

function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        if(response.status > 400 || response.status < 500) {
            return Promise.reject({ "status_code": response.status, "error": new Error(response.statusText), "response": response.json() })
        }
    }
}

function json(response) {
    return response.json()
}

function makeFetch(api_url, url, type, auth, content_type = undefined, data = undefined) {
    return fetch(api_url + url, {
        method: type,
        withCredentials: true,
        credentials: 'include',
        headers: new Headers({
            'Authorization': auth,
            'Content-type': content_type ? content_type :  "text/html",
            "Access-Control-Allow-Credentials": true
        }),
        body: data ? JSON.stringify(data) : undefined
    }

    )
        .then(status)
        .then(json)
        .then((data) => {
            console.log('Request succeeded with JSON response', data);
            return data;
        }).catch(function (error) {
            console.log('Request failed', error);
            store.addNotification({
                title: "An error has occurred.",
                //TODO: proper error messages from the api
                message: "For some reason.",
                type: "danger",
                insert: "top",
                container: "top-right",
                animationIn: ["animated", "fadeIn"],
                animationOut: ["animated", "fadeOut"],
                dismiss: {
                    duration: 10000,
                    onScreen: true
                }
            });
            throw error;
        });

}

class Vehicle {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
    }

    async getVehicles(user_id) {
        return makeFetch(this.api_url, "vehicles", "GET", this.bearer)
    }

    async getVehicle(vehicle_id) {
        return makeFetch(this.api_url, "vehicle/" + vehicle_id, "GET", this.bearer)
    }

    async createVehicle(input_data) {
        return makeFetch(this.api_url,  "vehicles", "POST", this.bearer, "application/json", input_data)
    }

    async updateVehicle(vehicle_id, input_data) {
        return makeFetch(this.api_url, "vehicle/" + vehicle_id, "PUT", this.bearer, "application/json", input_data)
    }

    async deleteVehicle(vehicle_id) {
        return makeFetch(this.api_url, "vehicle/" + vehicle_id, "DELETE", this.bearer, "application/json")
    }

    async restoreVehicle(vehicle_id) {
        return makeFetch(this.api_url, "vehicle/" + vehicle_id + "/restore", "PUT", this.bearer, "application/json")
    }
}

class Location {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
        this.availableLocations = [];
        /*makeFetch(this.api_url, "locations", "GET", this.bearer)
            .then((data) => {
                this.availableLocations = data;
            });*/
    }

    async getAvailableLocations() {
        return makeFetch(this.api_url, "locations", "GET", this.bearer);
        return new Promise((resolve, reject) => {
            resolve(this.availableLocations);
        });
    }

    async getLocation(location_id) {
        return makeFetch(this.api_url, "location/" + location_id, "GET", this.bearer)
    }

    async createLocation(input_data) {
        return makeFetch(this.api_url, "locations", "POST", this.bearer, "application/json", input_data)
    }
}

class Comment {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
    }

    async getComments(item_id) {
        return makeFetch(this.api_url, "comments/" + item_id, "GET", this.bearer)
    }

    async getComment(comment_id) {
        return makeFetch(this.api_url, "comment/" + comment_id, "GET", this.bearer)
    }

    async createComment(input_data) {
        return makeFetch(this.api_url, "comments", "POST", this.bearer, "application/json", input_data)
    }
    async updateComment(comment_id, input_data) {
        return makeFetch(this.api_url, "comment/" + comment_id, "PUT", this.bearer, "application/json", input_data)
    }
}

class Task {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
    }

    async getTasks(session_id) {
        return makeFetch(this.api_url, "tasks/" + session_id, "GET", this.bearer)
    }

    async getTask(task_id) {
        return makeFetch(this.api_url, "task/" + task_id, "GET", this.bearer)
    }

    async createTask(input_data) {
        return makeFetch(this.api_url, "tasks", "POST", this.bearer, "application/json", input_data)
    }

    async updateTask(task_id, input_data) {
        return makeFetch(this.api_url, "task/" + task_id, "PUT", this.bearer, "application/json", input_data)
    }

    async deleteTask(task_id) {
        return makeFetch(this.api_url, "task/" + task_id, "DELETE", this.bearer, "application/json")
    }

    async restoreTask(task_id) {
        return makeFetch(this.api_url, "task/" + task_id + "/restore", "PUT", this.bearer, "application/json")
    }
}

class Deliverable {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
        this.availableDeliverables = [];

        makeFetch(this.api_url, "deliverables/available", "GET", this.bearer, "application/json")
            .then((data) => {
                this.availableDeliverables = data;
            });
    }

    async getDeliverables(task_id) {
        return makeFetch(this.api_url, "deliverables/" + task_id, "GET", this.bearer)
    }

    async getDeliverable(deliverable_id) {
        return makeFetch(this.api_url, "deliverable/" + deliverable_id, "GET", this.bearer)
    }

    async createDeliverable(input_data) {
        return makeFetch(this.api_url, "deliverables", "POST", this.bearer, "application/json", input_data)
    }

    async updateDeliverable(deliverable_id, input_data) {
        return makeFetch(this.api_url, "deliverable/" + deliverable_id, "PUT", this.bearer, "application/json", input_data)
    }
    async getAvailableDeliverables() {
        return makeFetch(this.api_url, "deliverables/available", "GET", this.bearer, "application/json");
    }
}

class Session {
    constructor(bearer, api_url) {
        this.bearer = bearer;
        this.users = undefined;
        this.api_url = api_url;
    }

    async getSessions(user_id) {
        return makeFetch(this.api_url, "sessions/" + user_id, "GET", this.bearer)
    }

    async getSession(session_id) {
        return makeFetch(this.api_url, "session/" + session_id, "GET", this.bearer)
    }
    
    async getStatistics(session_id) {
        return makeFetch(this.api_url, "session/" + session_id + "/statistics", "GET", this.bearer)
    }

    async createSession(input_data) {
        if (input_data) {
            return makeFetch(this.api_url, "sessions", "POST", this.bearer, "application/json", input_data)
        }
        else  {
            return makeFetch(this.api_url, "sessions", "POST", this.bearer)
        }
    }
    async deleteSession(session_id) {
        return makeFetch(this.api_url, "session/" + session_id, "DELETE", this.bearer, "application/json")
    }

    async restoreSession(session_id) {
        return makeFetch(this.api_url, "session/" + session_id + "/restore", "PUT", this.bearer, "application/json")
    }

}

class Priority {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
        this.availablePriorities = [];

        /*makeFetch(this.api_url, "priorities", "GET", this.bearer)
            .then((data) => {
                this.availablePriorities = data;
            });*/
    }

    async getAvailablePriorities() {
        return makeFetch(this.api_url, "priorities", "GET", this.bearer);
        return new Promise((resolve, reject) => {
            resolve(this.availablePriorities);
        });
    }
}

class Patch {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.api_url = api_url;
    }

    async getAvailablePatches() {
        return makeFetch(this.api_url, "patches", "GET", this.bearer);
    }
}


class User {
    constructor(bearer, api_url){
        this.bearer = bearer;
        this.users = [];
        this.api_url = api_url;
    }

    async getUsers() {
        return makeFetch(this.api_url, "users", "GET", this.bearer);
    }

    async getUser(user_id) {
        return makeFetch(this.api_url, "user/" + user_id, "GET", this.bearer)

    }

    async createUser(input_data) {
        return makeFetch(this.api_url, "users", "POST", this.bearer, "application/json", input_data)
    }

    async getAssignedTasks(user_id) {
        return makeFetch(this.api_url, "user/" + user_id + '/tasks', "GET", this.bearer)
    }

    async whoami() {
        return makeFetch(this.api_url, 'whoami', "GET", this.bearer)
    }
}

class Control {
    constructor(api_url, bearer = undefined) {
        this.login = this.login.bind(this);
        this.initialiseClasses = this.initialiseClasses.bind(this);
        this.logout = this.logout.bind(this);
        this.ping = this.ping.bind(this);
        this.notifyDown = this.notifyDown.bind(this);
        this.notifyUp = this.notifyUp.bind(this);
        this.ping = this.ping.bind(this);
        this.api_url = api_url;
        this.token = "";
        this.bearer = "";
        this.connected = true;
        this.connectionReattempts = 0;

        if (bearer) {
            this.initialiseClasses(bearer)
        } else {
            this.sessions = undefined;
            this.notes = undefined;
            this.tasks = undefined;
            this.vehicles = undefined;
            this.initialised = false;
            this.users = undefined;
        }
    }

    async login(username, password) {
        return fetch(this.api_url + 'login', {
            method: 'post',
            headers: {
                "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: 'username=' + username + '&password=' + password
        })
    .then(status)
            .then(json)
            .then((data) => {
                console.log('Request succeeded with JSON response', data);
                return data;
            }).catch(function (error) {
                console.log('Request failed', error);
                store.addNotification({
                    title: "An error has occurred.",
                    //TODO: proper error messages from the api
                    message: "For some reason.",
                    type: "danger",
                    insert: "top",
                    container: "top-right",
                    animationIn: ["animated", "fadeIn"],
                    animationOut: ["animated", "fadeOut"],
                    dismiss: {
                        duration: 10000,
                        onScreen: true
                    }
                });
            });
    }

    ping() {
        let self = this;
        return fetch(this.api_url + 'ping', {
            method: 'get',
        })
            .then((response) => {
                if (response.status === 200) {
                    if (!this.connected) {
                        this.notifyUp();
                        this.connected = true;
                        this.connectionReattempts = 0;

                    }
                }
                else {
                    if (this.connected) {
                        this.connectionReattempts = 0;
                        this.connected = false;
                        this.notifyDown();
                    }
                    else {
                        if (this.connectionReattempts === 10) {
                            this.notifyDown();
                            this.connectionReattempts = 0;
                        }
                    }
                    this.connectionReattempts += 1;
                }
            })
            .catch(function (error) {
                if (self.connected) {
                    self.connectionReattempts = 0;
                    self.connected = false;
                    self.notifyDown();
                }
                else {
                    if (self.connectionReattempts === 10) {
                        self.notifyDown();
                        self.connectionReattempts = 0;
                    }
                }
                self.connectionReattempts += 1;
                console.log("Request failed", error);
            });
    }

    notifyDown() {
        store.addNotification({
            title: "Connection to the server has been lost.",
            message: "Check your internet connection.",
            type: "warning",
            insert: "top",
            container: "top-right",
            animationIn: ["animated", "fadeIn"],
            animationOut: ["animated", "fadeOut"],
            dismiss: {
                duration: 10000,
                onScreen: true
            }
        });

    }

    notifyUp() {
        store.addNotification({
            title: "Connection status.",
            message: "Connection has returned.",
            type: "success",
            insert: "top",
            container: "top-right",
            animationIn: ["animated", "fadeIn"],
            animationOut: ["animated", "fadeOut"],
            dismiss: {
                duration: 10000,
                onScreen: true
            }
        });
    }

    logout() {
        this.bearer = "";
        this.token = "";
        this.users = undefined;
        this.sessions = undefined;
        this.comments = undefined;
        this.tasks = undefined;
        this.deliverables = undefined;
        this.vehicles = undefined;
        this.locations = undefined;
        this.priorities = undefined;
        this.patches = undefined;
        this.initialised = false;
    }

    initialiseClasses(token) {
        this.bearer = "Bearer " + token;
        this.users = new User(this.bearer, this.api_url);
        this.sessions = new Session(this.bearer, this.api_url);
        this.comments = new Comment(this.bearer, this.api_url);
        this.tasks = new Task(this.bearer, this.api_url);
        this.deliverables = new Deliverable(this.bearer, this.api_url);
        this.vehicles = new Vehicle(this.bearer, this.api_url);
        this.locations = new Location(this.bearer, this.api_url);
        this.priorities = new Priority(this.bearer, this.api_url);
        this.patches = new Patch(this.bearer, this.api_url);
        this.initialised = true;
        //setInterval(this.ping, 4000);
    }
}

export default Control;