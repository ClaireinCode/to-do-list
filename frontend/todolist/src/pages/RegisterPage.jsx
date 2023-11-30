import {useEffect, useState} from 'react';
import {api} from '../utilities';
import { useNavigate } from 'react-router';

const RegisterPage = () => {
    const navigate = useNavigate();
    const [email, setEmail] =useState("");
    const [password, setPassword] = useState("");

    const signUp = async (e) => {
        e.preventDefault();
        // let userData = {email, password}
        // let response = await api.post("v1/users/signup/", userData)
        //     .catch(err => console.log(`signup err ${err}`))

        // let userEmail = response.data.user
        // let userToken = response.data.token

        // console.log(`signup success, email: ${userEmail}, token: ${token}`)

        // api.defaults.headers.common["Authorization"] = `Token ${token}`
        // localStorage.setItem("token", userToken)
        // localStorage.setItem("email", userEmail)
        navigate("/")
    }


    return (
        <>
            <div>
                <h2>Create an Account</h2>
                <form onSubmit={(e)=>signUp(e)}>
                <input
                    type="text"
                    placeholder="email"
                    onChange={(e)=> console.log(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="password"
                    onChange={(e)=> console.log(e.target.value)}
                />
                <input type="submit" value="Register"/>
                </form>
            </div>
        </>
    )
}
export default RegisterPage;