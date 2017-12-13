import { DIM_TOGGLE } from '../constants/actionTypes'

const initialState = {
        dimToggle : false
};


export default function uiReducer(state = initialState, action) {
  let newState;

  switch (action.type) {
    case DIM_TOGGLE:
          return {
            ...state,
            dimToggle: !state.dimToggle
          }

    case 'DO_NOTHING':
      newState = { ...state };
      // do something with the newstate
      return newState;

    default:
      return state;
  }
}
