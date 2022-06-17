import React, { Component } from 'react'
import Menu from './Menu'
import { Button, TextField, Typography } from '@material-ui/core'



export default class SignUp extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            email: "",
            password: "",
            error: ""
        }
        this.handleUsername = this.handleUsername.bind(this)
        this.handleEmail = this.handleEmail.bind(this)
        this.handlePswd = this.handlePswd.bind(this)
        this.handlePswdConfirmation = this.handlePswdConfirmation.bind(this)
        this.signUpButtonClicked = this.signUpButtonClicked.bind(this)
    }



    render() {
        return (
            <div className='container-login'>
                <div className='login-image'>
                    <img src='../static/images/login/login.jpg'></img>
                </div>
                <div className='login-form'>
                    <Typography className='login-text' variant='h4' component='h4' align='center'>Crie a sua conta</Typography>
                    <TextField className="login-input" label='Usuário' placeholder='Example Name' value={this.state.username} variant='outlined' onChange={this.handleUsername}></TextField>
                    <TextField className="login-input" label='Email' placeholder='example@mail.com' value={this.state.email} variant='outlined' onChange={this.handleEmail}></TextField>
                    <TextField className="login-input" label='Senha' type="password" placeholder="Senha" value={this.state.password} variant='outlined' onChange={this.handlePswd}></TextField>
                    <TextField className="login-input" label='Confirmar senha' type="password" placeholder="Senha" variant='outlined' helperText={this.state.error} error={this.state.error} onChange={this.handlePswdConfirmation}></TextField>
                    <Button className="login-button" variant='contained' color='primary' onClick={this.signUpButtonClicked}>Cadastrar</Button>
                </div>
            </div>

        )
    }

    handleUsername(e){
        this.setState({
            username: e.target.value
        })
    }

    handleEmail(e) {
        this.setState({
            email: e.target.value
        })
    }

    handlePswd(e) {
        this.setState({
            password: e.target.value
        })
    }

    handlePswdConfirmation(e){
        if (this.state.password != e.target.value){
            this.setState({error: "Por favor, verifique a senha. Elas precisam ser iguais."})
        } else {
            this.setState({error: ""})
        }

    }

    signUpButtonClicked() {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: this.state.username,
                email: this.state.email,
                password: this.state.password,
            }),
          };
        fetch('/user/cadastro', requestOptions)
        .then(() => this.props.history.push('/')) .then(() => location.reload())
    }
}