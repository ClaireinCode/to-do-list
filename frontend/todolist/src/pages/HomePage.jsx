import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {api} from '../utilities'


const HomePage = () => {
    const [currentLists, setCurrentLists] = useState([]);

    useEffect(() => {
        const getLists = async () => {
           
            let response = await api
                .get(`/v1/lists/`)
                .catch((err) => {console.log(err)});
            if (response && response.data) {
                setCurrentLists(response.data);
            }
            
        };
        getLists();
    }, []);

    ///////////////////////////////////////////////////////////////

    const [newList, setNewList] = useState("");

    const createNewList = async (e) => {
        e.preventDefault();
        console.log("check")
        let data = {
            list_name: newList
        }
        
        let response = await api
            .post(`v1/lists/`, data)
            .catch(err => console.log(err));
            console.log("back check")
        if (response.status === 201){
            window.location.reload();
        }
        else {
            console.log("something went wrong")
        }
        
    }

    return (
        <>
        <div>
            <div>
                <form onSubmit={createNewList}>
                <input 
                    type="text"
                    placeholder="List Name"
                    onChange={(e) => setNewList(e.target.value)}
                />
                <button type="submit">Create List</button>
                </form>
            </div>
            <ul>
                {currentLists.map((lists) => (
                <h4><Link to={`/lists/${lists.id}/`}>{lists.list_name}</Link></h4>
                ))}
            </ul>
        </div>
        </>
    )
}
export default HomePage