function    Button(props) {
    if(props.isLoggedIn) {
        return (
            <div className="flex justify-center items-center h-screen">
                <button className="bg-violet-200 border-3 justify-center items-center w-[200px] font-Roboto ">dfd </button>
            </div> 
        );
        
    }
    else {
        return (
         <div className="flex justify-center items-center h-screen">
                <button className="bg-violet-200 border-3 justify-center items-center w-[200px]   rounded-md hover:scale-101  cursor:pointer transition ease-in font-Roboto ">Login In {props.username} </button>
          </div>
        );
    }

}
export default Button