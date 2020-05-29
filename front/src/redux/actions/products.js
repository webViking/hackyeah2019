import axios from 'axios'
import * as actionTypes from './actionTypes'

const API_PRODUCTS_URL = "https://hackyeah-api.flyingarmageddon.pl/api/web/v1/get/policy"


export const fetchProductsStart = () =>{
    return{
        type: actionTypes.FETCH_PRODUCTS_BEGINN
    }
}

export const fetchProductsSuccess = (data) =>{
    return{
        type: actionTypes.FETCH_PRODUCTS_SUCCESS,
        data
    }
}
export const fetchProductsFail = (error) => {
    return{
        type: actionTypes.FETCH_PRODUCTS_FAIL,
        error
    }   
}


export const fetchProducts = () =>{
    return dispatch =>{
        dispatch(fetchProductsStart())
        axios.get(API_PRODUCTS_URL).then(response =>{
            dispatch(fetchProductsSuccess(response.data))
        }).catch(error =>{
            dispatch(fetchProductsFail(error))
        })
    }
}
