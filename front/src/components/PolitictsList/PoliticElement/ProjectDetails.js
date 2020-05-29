import React from 'react'
//import { connect } from 'react-redux'
//import * as actions from '../../../redux/actions/index'

import PoliticRule from './PoliticRule'
import "./PoliticElement.css"

class ProjectDetails extends React.Component{
  state = {
    data:[],
    count:1
  }
    componentDidMount(){
         console.log(this.props)
         fetch("https://hackyeah-api.flyingarmageddon.pl/api/web/v1/get/policy/" + this.props.match.params.id).then((res)=>{
          return res.json();
        }).then((json) => {
          console.log(json);
          this.setState({policies:json.data})
        })
      
  
    }
    delete(){
      
      fetch("https://hackyeah-api.flyingarmageddon.pl/api/web/v1/delete/policy/" + this.props.match.params.id).then((res)=>{
        return res.json();
      }).then((json) => {
        console.log(json);
        this.props.history.push("/")
      })
   
      
    }
    openRaport(){
      window.open(`https://hackyeah-api.flyingarmageddon.pl/api/web/v1/report/policy/${this.props.match.params.id}?ashtml`)
    }
    render(){

        if(!this.state.policies){
          return null;
        }
        console.log(this.state)
        return(
  
            <div className="py-5 mt-5">
            <div className="container policy_info">
              <h1 className="d-flex">Name: {this.state.policies[0].data.name}</h1>
              <h3 className="d-flex"> ID: {this.state.policies[0].id}
          </h3>
              <div className="row">
                <div className="col-12 mx-auto ">
                  <h4 className ="mb-3">Rules: </h4>
                  {this.state.policies[0].data.rules.map(el=>{
                    return <PoliticRule count = {this.state.count++}key = {el.name} el = {el}/>
                  })}
                </div>
              </div>
              <div>
                <div className = "col-12 col-md-12 mt-5">
                  <button className="btn btn-danger text-center text-white mx-auto mr-2 mt-2" onClick = {this.delete.bind(this)}><i className="fas fa-trash-alt"></i> Delete Policies</button>
                  <button className="btn btn-info text-center text-white mx-auto mr-2 mt-2" onClick ={this.openRaport.bind(this)}><i className="fas fa-file-alt"></i> Show Raport</button>
                </div>
              </div>
            </div>
          </div>
          
            
        )
    }
}
export default  ProjectDetails