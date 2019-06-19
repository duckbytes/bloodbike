import React, { Component } from "react";
import "./App.css";
import Header from "./components/header/header";
import List from "./containers/list/list";
import testData, { IJob } from "./test-data";
import Control from './api_control'

export interface IProps {
  filteredList: IJob[];
}

class App extends Component {
  public state = { filteredList: testData };
  public render() {
    // const modal = document.getElementById("myModal");
    // const infoIcon = document.getElementById("welcomeInfo");

    // infoIcon.onclick = modalToggled => {
    //   modalToggled.preventDefault();
    //   modal.style.display = "block";
    // };
    // window.onclick = event => {
    //   if (event.target === modal) {
    //     modal.style.display = "none";
    //   }
    // };

    return (
      <>
        <div id="myModal" className="modal">
          <div className="modal-content">
            <p>This is the welcome modal</p>
          </div>
        </div>
        <Header />
        <List filteredList={this.state.filteredList} />
      </>
    );
  }
}

export default App;
