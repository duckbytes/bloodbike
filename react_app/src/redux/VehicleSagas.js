import { throttle, call, put, takeEvery , takeLatest, select} from 'redux-saga/effects'
import {ADD_VEHICLE_REQUEST, addVehicleSuccess, UPDATE_VEHICLE_REQUEST, updateVehicleSuccess, GET_VEHICLES_REQUEST, getAllVehiclesSuccess, GET_VEHICLE_REQUEST, getVehicleSuccess} from "./Actions"
import { getApiControl } from "./Api";
// TODO: This needs to be adapted to vehicles!

function* postNewVehicle(action) {
    const api = yield select(getApiControl);
    const result = yield call([api, api.vehicles.createVehicle], action.data);
    const task = {...action.data, "uuid": result.uuid};
    yield put(addVehicleSuccess(task))
}

export function* watchPostNewVehicle() {
    yield takeEvery(ADD_VEHICLE_REQUEST, postNewVehicle)
}

function* updateVehicle(action) {
    const api = yield select(getApiControl);
    yield call([api, api.vehicles.updateVehicle], action.data.vehicleUUID, action.data.payload);
    yield put(updateVehicleSuccess(action.data))
}

export function* watchUpdateVehicle() {
    yield throttle(300, UPDATE_VEHICLE_REQUEST, updateVehicle)
}

function* getVehicles() {
    const api = yield select(getApiControl);
    const result = yield call([api, api.vehicles.getVehicles]);
    yield put(getAllVehiclesSuccess(result))
}

export function* watchGetVehicles() {
    yield takeLatest(GET_VEHICLES_REQUEST, getVehicles)
}

function* getVehicle(action) {
    const api = yield select(getApiControl);
    const result = yield call([api, api.vehicles.getVehicle], action.data);
    yield put(getVehicleSuccess(result))
}

export function* watchVehicle() {
    yield takeLatest(GET_VEHICLE_REQUEST, getVehicle)
}
