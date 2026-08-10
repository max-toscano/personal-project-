import Button from './Button.jsx';
import Header from './Header.jsx'
import Sidebar from './Sidebar.jsx'


function App() {
  return(
    <>
    <div className='flex min-h-screen bg-violet-200'>
      <Sidebar/>
      {/* Main content column sits next to the sidebar and takes the rest of the width */}
      <div className='flex-1'>
        <Header/>
        <Button isLoggedIn={false} username="spongebob"/>
      </div>
     </div>
    </>
  );
}
export default App 