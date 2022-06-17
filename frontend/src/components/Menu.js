import { Button } from "@material-ui/core";
import React, { Component } from "react";
import { Link } from "react-router-dom";
import Login from "./Login";

export default class Menu extends Component {
    constructor(props) {
        super(props)

        this.handleClick = this.handleClick.bind(this)
    }

    handleClick() {
        this.props.history.push('/login')
    }

    render() {
        return (
            <div className="menu">
                <div className='menu-logo'>
                    <img src='../../static/images/onlyLogo.png'></img>
                </div>
                <div className="center">
                    <div><a className="menu-item" href="/">Home</a></div>
                    <div><a className="menu-item" href='/cursos'>Cursos</a></div>
                    <div><a className="menu-item" href='/quem-somos'>Quem somos</a></div>
                </div>
                <div className="login">
                    <Button className='home-button'variant='contained' color='primary' onClick={() => 
                        location.href = '/login'
                    }>Login</Button>
                </div>
            </div>
        );
    }
}