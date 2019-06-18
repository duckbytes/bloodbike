import React, { Component } from "react";
import "./App.css";
import Header from "./components/header/header";
import List from "./containers/list/list";
import testData, { IJob } from "./test-data";
import Control from "./fetches.js"

export interface IProps {
  filteredList: IJob[];
}

class App extends Component {
  public state = {
      api_control: new Control({"api_url": "/api/v0.1/"}),

  };
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

      this.state.api_control.login("admin", "asdfasdf");
      let session_data = this.state.api_control.sessions.get_session("f6479de6-0c8b-4290-b1b0-458b3bd5d443");

    return (
      <>
        <div id="myModal" className="modal">
          <div className="modal-content">
            <p>This is the welcome modal</p>
          </div>
        </div>
        <Header />
        <List filteredList={session_data} />
      </>
    );
  }
}

export default App;
