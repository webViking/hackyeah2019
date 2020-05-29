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
        console.log("test")
        const data = {
            name: this.state.nameString,
            id: this.state.id,
        }

        axios.post("https://hackyeah-api.flyingarmageddon.pl/api/client/v1/add/device ",data).then(res=>{
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
                    <h1 className="d-flex justify-content-center text-center mb-5">Add new Computer</h1>
                    
                    <div className="row">
                    <div className="md-form mt-2 cold-md-6 d-flex justify-content-center mx-auto" style={{ width: "20rem" }}>
                        <input value={this.state.nameString} onChange={this.onChangeHandlerName.bind(this)} className="form-control mb-5 text-center" type="text" placeholder="Enter the name of computer" aria-label="Post" />
                    </div>
                    </div>
                    <div className="row">
                        <div className="md-form mt-2 cold-md-6 d-flex justify-content-center mx-auto" style={{ width: "20rem" }}>
                        <input value={this.state.id} onChange={this.onChangeHandlerId.bind(this)} className="form-control mb-5 text-center" type="text" placeholder="Enter an ID of computer" aria-label="Post" />
                        </div>
                    </div>
                    
                    
                    </div>
                    <div className = "col-6 col-md-3 col-md-offset-5 pb-5 mx-auto ">
                  <button type ="submit" onClick ={this.handleSubmit.bind(this)} className="btn btn-success text-center text-white">Submit new Computer</button>
                </div>
            </div>
            </div>
        )
    }
    
}
export default NewPolitic