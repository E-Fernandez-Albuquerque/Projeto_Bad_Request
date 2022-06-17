import React, {Component} from "react"
import { render } from "react-dom"
import Menu from './Menu'
import HomePage from "./HomePage"

export default class App extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="page">
                <HomePage></HomePage>
            </div>
        )
    }
}

const appDiv = document.getElementById('app')
render(<App />, appDiv)