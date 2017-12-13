import axios from 'axios'
import * as types from '../constants/actionTypes';


export function dimToggle() {
  return { type: types.DIM_TOGGLE };
}

export function searchMeme(query) {
  return (dispatch)=> {
    axios.get(`http://138.197.42.109:8000/api/search/?format=json&q=${query}`)
         .then(res => {
            dispatch({
              type: types.FETCH_MEMES,
              payload: res.data
            });
         })
         .catch(err => {
            // let it go for now
         })
  };
}


export function doNothing(payload) {
  return (dispatch)=> {
    dispatch({
      type: 'DO_NOTHING',
      payload
    });
  };
}
