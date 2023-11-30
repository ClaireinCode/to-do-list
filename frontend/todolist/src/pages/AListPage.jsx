import {useEffect, useState} from 'react';
import {useParams} from 'react-router-dom';
import axios from 'axios'

const AListPage = () => {
    const {id} = useParams();
    const [aList, setAList] = useState(null);

    useEffect(() => {
        const getAList = async () => {
            let response = await axios.get(
                `http://127.0.0.1:8000/api/v1/lists/${id}/`
            );
            setAList(response.data);
        };
        getAList();
    }, []);

    ///////////////////////////////////////////////////////////////

    

    return (
        <>
        <h3>{aList.list_name}</h3>
        <div>
        {aList ? aList : null}
        </div>
        </>
    )
}

export default AListPage;