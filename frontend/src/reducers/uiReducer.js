import { DIM_TOGGLE, FETCH_MEMES } from '../constants/actionTypes'

const initialState = {
        dimToggle : false,
        memeList: []
};


export default function uiReducer(state = initialState, action) {
  let newState;

  switch (action.type) {
    case DIM_TOGGLE:
          return {
            ...state,
            dimToggle: !state.dimToggle
          }
    case FETCH_MEMES:
          return {
            ...state,
            memeList: action.payload
          }

    case 'DO_NOTHING':
      newState = { ...state };
      // do something with the newstate
      return newState;

    default:
      return state;
  }
}
