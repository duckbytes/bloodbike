import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {BrowserRouter} from 'react-router-dom'
import ReactNotification from 'react-notifications-component'
import 'react-notifications-component/dist/theme.css'
import {Provider} from 'react-redux'
import store from "./redux/Store"

window.store = store;


const apiUrl = 'https://bloodbike-api.herokuapp.com/api/v0.1/';

ReactDOM.render((
        <Provider store={store}>
            <BrowserRouter>
                <ReactNotification/>
                <App apiUrl={apiUrl}/>
            </BrowserRouter>
        </Provider>),
    document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

