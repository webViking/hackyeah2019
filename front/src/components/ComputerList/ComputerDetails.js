import React from 'react'


import "./ComputerDetails.css"

class ProjectDetails extends React.Component{
  state = {
    data:[],
    count:1
  }
    componentDidMount(){
         console.log(this.props)
         fetch("https://hackyeah-api.flyingarmageddon.pl/api/web/v1/get/device/" + this.props.match.params.id).then((res)=>{
          return res.json();
        }).then((json) => {
          console.log(json);
          this.setState({devices:json.data})
        })
      
  
    }
    delete(){
      
      fetch("https://hackyeah-api.flyingarmageddon.pl/api/web/v1/get/device/" + this.props.match.params.id).then((res)=>{
        return res.json();
      }).then((json) => {
        console.log(json);
        this.props.history.push("/")
      })
   
      
    }
    render(){

        if(!this.state.devices){
          return null;
        }
        console.log(this.state)
        return(
  
            <div className="py-5 mt-5">
            <div className="container policy_info">
              <h1 className="d-flex">Name: {this.state.devices[0].data.name}</h1>
              <h3 className="d-flex"> ID: {this.state.devices[0].id}
          </h3>
              <div className="row">
  
              </div>
              <div>
                <div className = "col-12 col-md-12 mt-5">
                  <button className="btn btn-danger text-center text-white mx-auto mr-2 mt-2" onClick = {this.delete.bind(this)}><i className="fas fa-trash-alt"></i> Delete computer</button>
                </div>
              </div>
            </div>
          </div>
          
            
        )
    }
}
export default  ProjectDetails