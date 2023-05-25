import React, { useState } from "react";
import '../css/Forget1.css';
import { Link } from "react-router-dom";
const Forgot1 = () => {
  const [email, setEmail] = useState("");
  const [msg, setMsg] = useState();



  const [error, setError] = useState(false)
  const validation = (e) => {
    e.preventDefault();
    if (email.length === 0) {
      setError(true)
    }
  }



  const postUser = () => {
    let item = { email }
    console.log(item)
    const requestOptions = {
      method: 'POST',
      headers:
      {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(
        (item)
      ),
    };

    fetch(
      'http://35.90.113.221/forget_password/',
      requestOptions,
    )
      .then(detail => detail.json())
      .then(resp => {
        if (resp) {
          if (resp.message === "Reset Password Email has been sent to your Email ID") {
            setMsg(resp.message)
          }
          else {
            setMsg(resp.message)
          }
          console.log('item post ', resp)
        }
      })
      .catch(error => {
        console.error(error);
      });
  };
  return (
    <>
      {/* Sign in form start */}

      <div className="container-fluid">
        <div className="row">
          <div className="col-sm-4 forgotdiv4">
            <div className="card forgotcard">
              <img src="images\logo.png" className="forgotlogo" />
              <h1><b>Hi, Welcome Back</b></h1>
              <img src="images\illustration_login.png" className="forgotbook" />
            </div>
          </div>

          <div className="col-sm-8 forgotdiv8">
            <p className="forgotcreateaccount">Don't have an account? <Link to="/"><b><span style={{ color: "#f45ca5" }}>Get started</span></b></Link></p>
            <h1>Enter Email address</h1>
            <p className="forgotenterdetail">Link will be sent on email address. </p>
            <p className="forgeterror">{msg}</p>
            <form onSubmit={validation}>
              <input type="email" className="form-control forgetemail" placeholder="Enter Email Address :" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
              {error && email.length <= 0 ? <label className="forgotemaillabel"> Email can't be empty.</label> : ""}

              <button onClick={postUser} type="submit" className="forgetsubmit"><b style={{ color: "white" }}>Submit</b></button>
            </form>
          </div>
        </div>
      </div>
      {/* Sign in form End */}
    </>
  )
}
export default Forgot1;
export async function postUser(user) {
  // send a POST request to a server to create a new user
}
