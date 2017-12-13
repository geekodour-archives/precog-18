import * as types from '../constants/actionTypes';


export function dimToggle() {
  return { type: types.DIM_TOGGLE };
}


export function doNothing(payload) {
  return (dispatch)=> {
    dispatch({
      type: 'DO_NOTHING',
      payload
    });
  };
}
