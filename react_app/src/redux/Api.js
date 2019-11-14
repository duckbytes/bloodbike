import Control from "../ApiControl";
import {deleteLogin, getLogin} from "../utilities";

const apiUrl = 'https://bloodbike-api.herokuapp.com/api/v0.1/';
let savedBearer = getLogin();
const api = new Control(apiUrl, savedBearer);
export default api;
