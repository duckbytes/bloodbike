import {GET_AVAILABLE_PATCHES_SUCCESS} from "./PatchesActions";

export function availablePatches(state = [], action) {
    switch (action.type) {
        case GET_AVAILABLE_PATCHES_SUCCESS:
            return action.data;
        default:
            return state
    }
}
