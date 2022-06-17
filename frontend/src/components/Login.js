import React, { Component } from 'react'
import Menu from './Menu'
import { Button, TextField, Typography } from '@material-ui/core'



export default class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: "",
        }
        this.handleUsername = this.handleUsername.bind(this)
        this.handlePswd = this.handlePswd.bind(this)
        this.loginButtonClicked = this.loginButtonClicked.bind(this)
    }



    render() {
        return (
            <div className='container-login'>
                <div className='login-image'>
                    <img src='../static/images/login/login.jpg'></img>
                </div>
                <div className='login-form'>
                    <Typography className='login-text' variant='h4' component='h4' align='center'>Acessando o mundo da <b>Tecnologia</b></Typography>
                    <TextField className="login-input" label='Usuário' placeholder='Nome de usuário' value={this.state.username} variant='outlined' onChange={this.handleUsername}></TextField>
                    <TextField className="login-input" label='Senha' type="password" placeholder="Senha" value={this.state.password} variant='outlined' onChange={this.handlePswd}></TextField>
                    <Button className="login-button" variant='contained' color='primary' onClick={this.loginButtonClicked}>Login</Button>
                    <a id='signup' href='/cadastro'>Sem conta? Cadastre-se aqui!</a>
                </div>
            </div>

        )
    }

    handleUsername(e) {
        this.setState({
            username: e.target.value
        })
    }

    handlePswd(e) {
        this.setState({
            password: e.target.value
        })
    }

    loginButtonClicked() {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              username: this.state.username,
              password: this.state.password,
            }),
          };
        fetch('/user/login', requestOptions)
        .then(() => this.props.history.push('/')).then(() => location.reload())
    }
}