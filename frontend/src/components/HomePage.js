import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from '@material-ui/core'
import Menu from "./Menu";
import Login from "./Login";
import About from "./About";
import Courses from "./Courses";
import SignUp from "./SignUp";

export default class HomePage extends Component {
    constructor(props) {
        super(props)
    }

    renderHomePage() {
        return (
            <div className="home-container">
                <div className='home-container-1'>
                    <div className='home-container-2'>
                        <img src='./static/images/logo.png'></img>
                        <h2>Somos uma escola online focada no ensino da programação</h2>
                        <h2>Visamos a equidade no ensino por meio de cursos acessíveis e de qualidade</h2>
                        <Button className="home-about" variant='contained' color='white' onClick={() => 
                        location.href = '/quem-somos'
                    }>Conhecer</Button>
                    </div>
                    <img className='landing-image' src="./static/images/home/brain.png"></img>
                </div>
            </div>
            
        )
    }

    render() {
        return (
            <>
                {/* <Menu></Menu> */}
                <Router>
                    <Switch>
                        <Route exact path="/" render={() => {
                            return this.renderHomePage()
                        }}></Route>
                        <Route path="/quem-somos" component={About}></Route>
                        <Route path="/login" component={Login}></Route>
                        <Route path="/cursos" component={Courses}></Route>
                        <Route path='/cadastro' component={SignUp}></Route>
                    </Switch>
                </Router>
            </>


        );
    }
}