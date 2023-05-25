import React, { useState } from "react";
import '../css/Login.css';
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom"

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const [msg, setMsg] = useState();


  const [error, setError] = useState(false)
  const validation = (e) => {
    e.preventDefault();
    if (password.length === 0 || email.length === 0) {
      setError(true)
    }
  }

  const postUser = () => {
    let item = { email, password }
    // console.log(item)
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify(
        (item)
      ),
    };

    fetch(
      'http://35.90.113.221/login/',
      requestOptions,
    )
      .then(detail => detail.json())
      .then(resp => {
        if (resp) {
          if (resp.user_id) {
            localStorage.setItem('user', JSON.stringify(resp));
            // console.log(resp.access)
            navigate("/Blog")
          }
          else {
            setMsg(resp.message)
          }
          // console.log('item post ', resp)
        }
      })
      .catch(error => {
        // console.error(error);
      });
  };
  return (
    <>
      <div className="container-fluid ">
        <div className="row">
          <div className="col-sm-4 logindiv4 ">
            <div className="card logincard">
              <img src="images\logo.png" className="loginlogo" />
              <h1><b>Hi, Welcome Back</b></h1>
              <img src="images\illustration_login.png" className="loginbook" />
            </div>
          </div>

          <div className="col-sm-8 logindiv8 ">
            <p className="logincreateaccount">Don't have an account? <Link to="/Register"><b><span style={{ color: "#f45ca5" }}>Get started</span></b></Link></p>

            <h1>Sign in to My App</h1>



            <p className="loginenterdetail">Enter your details below.</p>
            <p className="backendresp">{msg}</p>
            <form onSubmit={validation}>

              <input type="email" className="form-control loginemail" placeholder="Email Id:" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
              {error && email.length <= 0 ? <label className="loginemaillabel"> Email can't be empty.</label> : ""}

              <input type="password" className="form-control loginpwd" placeholder="Password:" name="pwd" value={password} onChange={(e) => setPassword(e.target.value)} />
              {error && password.length < 8 ? <label className="loginpwdlabel">Password must be 8 Characters.</label> : ""}

              <button onClick={postUser} type="submit" className=" loginsubmit"><b style={{ color: "white" }}>Login</b></button>

            </form>

            <input className="loginremember" type="checkbox" />

            <p id="rme">Remember me</p>

            <Link to="/Forgot1"><p style={{ color: "#f45ca5" }} id="loginforgot" href="#">Forgot password?</p></Link>
          </div>
        </div>
      </div>
    </>
  )
}
export default Login;