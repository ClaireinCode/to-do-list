import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import ListsPage from "./pages/ListsPage";
import RegisterPage from "./pages/RegisterPage";


const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <HomePage/>,
            },
            {
                path: 'lists/',
                element: <ListsPage/>,
            },
            {
                path: 'register',
                element: <RegisterPage/>,
            }
        ]
    }
]);

export default router;