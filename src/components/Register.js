import React, { useState } from "react";
import '../css/Register.css';
import { Link, } from "react-router-dom";
import { useNavigate } from "react-router-dom"



const Register = () => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [first_name, setFirst] = useState("");
  const [last_name, setLast] = useState("");
  const [number] = useState("");
  const navigate = useNavigate();
  const [msg, setMsg] = useState();


  // VALIDATION CODE START
  const [error, setError] = useState(false)
  const validation = (e) => {
    e.preventDefault();
    if (first_name.length === 0 || last_name.length === 0 || username.length === 0 || password.length === 0 || email.length === 0) {
      setError(true)
    }
  }
  // VALIDATION CODE END

  const postUser = () => {
    let item = { email, username, password, first_name, last_name, number }
    // console.log(item)
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(
        (item)
      ),
    };

    fetch(
      'http://35.90.113.221/register/',
      requestOptions,
    )
      .then(detail => detail.json())
      .then(resp => {
        if (resp) {
          if (resp.user_id) {
            localStorage.setItem('user', JSON.stringify(resp));
            // console.log(resp.access)
            navigate("/About_social")
          }
          else {
            if (resp.email) {
              setMsg(resp.email)
            }
            else {
              setMsg(resp.username)
            }
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
      <div className="container-fluid">
        <div className="row">
          <div className="col-sm-4 div4 ">
            <div className="card signincard">
              <img src="images\logo.png" className="logo" alt="no image" />
              <h1><b>Manage the job more effectively with My App</b></h1>
              <img src="images\illustration_register.png" className="book" alt="" />
            </div>
          </div>

          <div className="col-sm-8  registerdiv8 ">
            <p className="registercreateaccount">Already have an account? <Link to="/Login"><b><span className="l" style={{ color: "#f45ca5" }}>Login</span></b></Link></p>
            <h1 id="registerdiv8h1">Get started absolutely free.</h1>
            <p id="enterdetail">Free forever. No credit card needed..</p>
            <p className="backend">{msg}</p>

            <form onSubmit={validation}>
              <input type="text" className="form-control registerfname" placeholder="First Name:" name="email" value={first_name} onChange={(e) => setFirst(e.target.value)} />
              {error && first_name.length <= 0 ? <label className="fnamelabel">First Name Can't Be Empty.</label> : ""}

              <input type="text" className="form-control registerlname" placeholder="Last Name:" name="email" value={last_name} onChange={(e) => setLast(e.target.value)} />
              {error && last_name.length <= 0 ? <label className="lnamelabel">Last name can't be empty.</label> : ""}

              <input type="email" className="form-control email" placeholder="Email Id:" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
              {error && email.length <= 0 ? <label className="emaillabel"> Email can't be empty.</label> : ""}

              <input className="form-control username" type="text" placeholder="Username:" value={username} onChange={(e) => setUsername(e.target.value)} /><br /><br />
              {error && username.length <= 0 ? <label className="usernamelabel">Username can't be empty.</label> : ""}

              <input type="password" className="form-control pwd" placeholder="Password:" name="pwd" value={password} onChange={(e) => setPassword(e.target.value)} />
              {error && password.length < 8 ? <label className="passwordlabel">Password must be 8 Characters.</label> : ""}

              <button onClick={postUser} type="submit" className="submit"><b style={{ color: "white" }}>Register</b></button>
            </form>

            <p className="lastpara">By registering, I agree to Minimal <span><a style={{ color: "black" }} href="">Terms of Service</a></span> and<span><a style={{ color: "black" }} href=""> Privacy Policy.</a></span></p>
          </div>
        </div>
      </div>
    </>
  )
}
export default Register;