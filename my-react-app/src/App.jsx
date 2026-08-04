import Button from './Button.jsx';
import Header from './Header.jsx'


function App() {
  return(
    <>
    <div className='min-h-screen bg-violet-200'> 
      <Header/> 
      <Button isLoggedIn={false} username="spongebob"/>
      
     </div> 
    </>
  );
}
export default App 