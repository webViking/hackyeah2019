import axios from 'axios'
import * as actionTypes from './actionTypes'

const API_DEVICES_URL = "https://hackyeah-api.flyingarmageddon.pl/api/web/v1/get/device"


export const fetch_deviceStart = () =>{
    return{
        type: actionTypes.FETCH_DEVICES_BEGINN
    }
}

export const fetch_deviceSuccess = (data) =>{
    return{
        type: actionTypes.FETCH_DEVICES_SUCCESS,
        data
    }
}
export const fetch_deviceSFail = (error) => {
    return{
        type: actionTypes.FETCH_DEVICES_FAIL,
        error
    }   
}


export const fetchDevices = () =>{
    return dispatch =>{
        dispatch(fetch_deviceStart())
        axios.get(API_DEVICES_URL).then(response =>{
            console.log(response.data)
            dispatch(fetch_deviceSuccess(response.data))
        }).catch(error =>{
            dispatch(fetch_deviceSFail(error))
        })
    }
}
