import React from "react";
import { Outlet } from "react-router-dom";
import './studentdashboard.css';
import Navbar from "../../Components/Navbar/Navbar";
import Sidebar from "../../Components/Sidebar/Sidebar";



const LecturerDashboard = () => {
    return (
            <div className="dashboard-container">
                <h1>
                    <h1>Lecturer Dashboard</h1>
                </h1>
                <Navbar />
                <Sidebar />
                <div className="dashboard-content">
                    <Outlet/>
                </div>
            </div>
       
    );
};

export default LecturerDashboard;