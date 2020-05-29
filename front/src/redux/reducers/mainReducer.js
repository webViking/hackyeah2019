import * as actionTypes from '../actions/actionTypes'
const initialState = {
    products: [],
    loading: false,
    error: null,
    devices:[]
}

const mainReducer = (state = initialState, action) => {

    switch (action.type) {
        case actionTypes.FETCH_PRODUCTS_BEGINN:
            return {
                ...state,
                loading: true
            }
        case actionTypes.FETCH_PRODUCTS_FAIL:
            return {
                ...state,
                error: action.error
            }
        case actionTypes.FETCH_PRODUCTS_SUCCESS:
        return {
                ...state,
                products: action.data,
                loading: false,
            }
            case actionTypes.FETCH_DEVICES_BEGINN:
                return{
                    ...state,
                    loading:true
                }
            case actionTypes.FETCH_DEVICES_SUCCESS:{
                return{
                    ...state,
                    loading:false,
                    devices: action.data
                }
            }    
            case actionTypes.FETCH_DEVICES_FAIL:
                return{
                    ...state,
                    loading:false,
                    error: action.error
                }    
            case actionTypes.FETCH_DEVICES:
                return{
                    ...state,
                    loading:false,
                
                }
        default:
            return state
    }
}
export default mainReducer