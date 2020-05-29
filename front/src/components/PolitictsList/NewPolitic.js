import React from 'react'
import axios from 'axios'
class NewPolitic extends React.Component{
    state = {
        nameString : "",
        id:"",
        textarea:""
    }
    onChangeHandlerName(e){
        this.setState({nameString:e.target.value})
    }
    onChangeHandlerId(e){
        this.setState({ id: e.target.value, })
    }
    onChangeHandlerTextarea(e){
        this.setState({textarea:e.target.value })
    }
    handleSubmit(event){
        console.log("testr")
        const data = {
            name: this.state.nameString,
            id: this.state.id,
            rules:JSON.parse(this.state.textarea),
            assigned_to: [123]
        }

        axios.post("https://hackyeah-api.flyingarmageddon.pl/api/client/v1/add/policy",data).then(res=>{
            console.log(res)
            this.props.history.push('/')
        }).catch(err=>{
            console.log(err)
        })
        event.preventDefault()
    }
    render(){
        return(
            <div className="py-5 mt-5">
                <div className="container policy_info">
                    <div className="col-12 col-md-8 mx-auto">
                    <h1 className="d-flex justify-content-center text-center mb-5">Add new policy</h1>
                    
                    <div className="row">
                    <div className="md-form mt-2 cold-md-6 d-flex justify-content-center mx-auto" style={{ width: "20rem" }}>
                        <input value={this.state.nameString} onChange={this.onChangeHandlerName.bind(this)} className="form-control mb-5 text-center" type="text" placeholder="Enter the name of policy" aria-label="Post" />
                    </div>
                    </div>
                    <div className="row">
                        <div className="md-form mt-2 cold-md-6 d-flex justify-content-center mx-auto" style={{ width: "20rem" }}>
                        <input value={this.state.id} onChange={this.onChangeHandlerId.bind(this)} className="form-control mb-5 text-center" type="text" placeholder="Enter an ID" aria-label="Post" />
                        </div>
                    </div>
                    
                    <div className = "row">
                    <div className="md-form mt-2 cold-md-6 d-flex justify-content-center mx-auto" style={{ width: "30rem",height:"20rem" }}>
                        <textarea value={this.state.textarea} onChange={this.onChangeHandlerTextarea.bind(this)} className="form-control mx-auto mb-5 text-center" type="text" placeholder="Enter rules (json format) I trust you" aria-label="Post" />
                    
                    </div>
                   
                    </div>
                    
                    </div>
                    <div className = "col-6 col-md-2 pb-3 col-md-offset-5 mx-auto ">
                  <button type ="submit" onClick ={this.handleSubmit.bind(this)} className="btn btn-success text-center text-white">Submit new policy</button>
                </div>
            </div>
            </div>
        )
    }
    
}
export default NewPolitic