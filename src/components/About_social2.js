import React, { useState } from "react";
import '../css/About_social2.css';
import '../css/Login.css';
import { Link } from "react-router-dom";

const About_social2 = () => {

  var user_token = JSON.parse(localStorage.getItem('user'));
  const [user, setUser] = useState(user_token.user_id);
  const [linkedin, setLinkedin] = useState("");
  const [twitter, setTwitter] = useState("");
  const [instagram, setInstagram] = useState("");
  const [facebook, setFacebook] = useState("");

  const postUser = () => {
    let token = user_token.access
    let item = { user, linkedin, twitter, instagram, facebook }
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        Authorization:
          'Bearer ' + token,
      },
      body: JSON.stringify(
        (item)
      ),
    };

    fetch(
      'http://35.90.113.221/user_social/',
      requestOptions,
    )
      .then(detail => detail.json())
      .then(resp => {
        if (resp) {
          console.log('item post ', resp)
        }
      })
      .catch(error => {
        console.error(error);
      });
  };
  return (
    <>
      <div className="container-fluid">
        <div className="row">
          <div className="col-sm-4 div4">
            <div className="card signincard">
              <img src="images\logo.png" className="logo" />
              <h1><b>Hi, Welcome Back</b></h1>
              <img src="images\illustration_login.png" className="book" />
            </div>
          </div>

          <div className="col-sm-8 div8">
            <h1 className="socialdetailh1">Social details</h1>
            <input type="text" className="form-control about1" placeholder="Linkedin:" name="linkedin" value={linkedin} onChange={(e) => setLinkedin(e.target.value)} />
            <input type="text" className="form-control about2" placeholder="Twitter:" name="twitter" value={twitter} onChange={(e) => setTwitter(e.target.value)} />
            <input type="text" className="form-control about3" placeholder="Instagram:" name="instagram" value={instagram} onChange={(e) => setInstagram(e.target.value)} />
            <input type="text" className="form-control about4" placeholder="facebook:" name="facebook" value={facebook} onChange={(e) => setFacebook(e.target.value)} />
            <Link to="/Profilepic"><button onClick={postUser} type="submit" className="btn aboutsubmit"><b style={{ color: "white" }}>Submit</b></button></Link>
          </div>
        </div>
      </div>
    </>
  )
}
export default About_social2;