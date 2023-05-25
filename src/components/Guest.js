import React from 'react'
import Navbar from "./Navbar";
import '../css/Blog.css';
import SearchIcon from '@mui/icons-material/Search';
import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import AddIcon from '@mui/icons-material/Add';
import TextsmsRoundedIcon from '@mui/icons-material/TextsmsRounded';
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import Zoom from 'react-reveal/Zoom';
import CircularProgress from '@material-ui/core/CircularProgress';
import GroupIcon from '@mui/icons-material/Group';
const Guest = () => {

    // var user_token = JSON.parse(localStorage.getItem('user'));
    // console.log(user_token)
    // let token = user_token.access
    const [blog, setBlog] = useState([]);
    const [post, setPost] = useState(null)
    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            redirect: 'follow',
            headers: {
                'Content-Type': 'application/json',
                Accept: 'application/json',
                // Authorization:
                //     'Bearer ' + token,
            },
        };

        fetch(
            'http://35.90.113.221/view_all_posts/',

            requestOptions,
        ).then(resp => {
            const { body } = resp
            setPost(body)
            resp.json().then(resp => {
                // console.log(resp);
                setBlog(resp);

            });
        });
    }, []);

    return (
        <>
            {post ?
                <div className="container-fluid ">
                    <div className="row">
                        <div className="col-lg-12  sticky-top">
                            <ul style={{ listStyle: "none" }}>
                                <li><a className="nav-link" href="#"><SearchIcon className="navsearch" /></a></li>
                                <li><a className="nav-link" href="#"><GroupIcon className="navgroup" /></a></li>
                                <li><a className="nav-link" href="#"><img className="navflag" src="\images\us.png" /> </a></li>
                            </ul>
                        </div>
                        <div className="col-sm-12 ">

                            <h4 className="h4profile">Blog</h4>
                            <a href="#" className="dashboard">Dashboard</a>
                            <FiberManualRecordIcon className="dot1" />
                            <a href="#" className="user">Blog</a>
                            <FiberManualRecordIcon className="dot2" />
                            <p className="ui">New Post</p>
                            <Link to="/New_post"> <button className="btn pluspostbutton"><AddIcon className="addicon" />New Post</button></Link>
                            <SearchIcon className="blogsearchicon" /><input className="searchpost" type="Search" placeholder="Search post..."></input>
                            <select className="blogselect">
                                <option>Latest</option>
                                <option>Populer</option>
                                <option>Oldest</option>
                            </select>

                            {/*CARD START */}
                            <div className="fcontainer">
                                {
                                    blog.map((item, j) =>
                                        <Zoom key={j}>
                                            <div className='fitem'>
                                                <Link style={{ textDecoration: "none" }} to="/Login">
                                                    <img className="blog4img1" src={'http://35.90.113.221' + item.user.user.images}></img>
                                                    <img style={{ width: 311, height: 200 }} src={'http://35.90.113.221' + item.images} className="blog4img2"></img>
                                                    <p className="blog4p1">{item.post_name}</p>
                                                    <p style={{ color: "black" }} className="blog4p2">{item.tag_name}</p>
                                                    <TextsmsRoundedIcon className="blog4commenticon w3-large" /><p className="blog4commenticonp">9.30k</p>
                                                </Link>
                                            </div>
                                        </Zoom>
                                    )}
                            </div>
                        </div>
                    </div>
                </div>
                : <CircularProgress style={{ width: 80, height: 80, position: "absolute", left: "45%", top: "35%", color: "#f45ca5" }} />}
        </>
    )
}
export default Guest