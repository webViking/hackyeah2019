import React, { Component } from 'react'
import { connect } from 'react-redux'
import ComputerElement from './ComputerElement/ComputerElement'
import * as actions from '../../redux/actions/index'

export class PolitictsList extends Component{
    state = {
        searchString: "",
    }
    onChangeHandler = (e) => {
        this.setState({ searchString: e.target.value })
    }
    componentDidMount() {
        this.props.onFetchDevices()
        console.log(this.props.productsList)
      }
    render(){
      console.log(this.props)
       const filtredElements = this.props.productsList.data && this.props.productsList.data.filter(el => {
            if (!el.data) return false;
            return el.data.name.toLowerCase().indexOf(this.state.searchString.toLowerCase()) !== -1
         })
         

        return(
            <div className="py-5 mt-5">
            <div className="container">
              <h1 className="d-flex justify-content-center text-center mb-5">Find your Devices!</h1>
              
                <div className="col-12 col-md-8 mx-auto">
                  
               {/* 
               <div className = "md-form mt-2 mx-auto d-flex justify-content-center mb-5">
              <button className="btn btn-info text-center text-white mx-auto mr-2 mt-2">Add new policies</button>
                </div>
              */}   
                <h5 className="d-flex justify-content-center text-center mb-5">Enter the name of device</h5> 
              <div className="row">
                  <div className="md-form mt-2 mx-auto d-flex justify-content-center" style={{ width: "20rem" }}>
                    <input value={this.state.searchString} onChange={this.onChangeHandler} className="form-control mb-5 text-center" type="text" placeholder="Enter your policy name" aria-label="Search" />
                  </div>
                </div>
              </div>
              <div>
               
              </div>
              <div className="row">
                {
                  filtredElements && filtredElements.map((items) => {
                  
                    
                
                    return  <ComputerElement key = {items.id} items = {items} /> 
                  
                     
                  
                  })
                }
              </div>
            </div>
          </div>
        )
    }
}
const mapStateToProps = (state) => {
  return {
      productsList: state.products.devices
    }
  }
  const mapDispatchToProps = (dispatch) => {
    return {
      onFetchDevices: () => dispatch(actions.fetchDevices())
    }
  }
export default connect(mapStateToProps,mapDispatchToProps)(PolitictsList);