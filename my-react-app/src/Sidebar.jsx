import { useState
 } from "react"; 

import {
    PanelLeftClose,
    PanelLeftOpen,
    Car, // used cars
    Boxes, //this is the boxes that will be used for the parts 
    Settings, //settings tab 
    UserRoundSearch,  // the active user tab 
} from "lucide-react"; 

// ai notes is above 

const Nav = [
    { icon: Boxes, label: "Parts" },
    { icon: Settings, label: "Setting" },
    { icon: UserRoundSearch, label: "Users" },
    { icon: Car, label: "Cars" },
];



export default function Sidebar() {
    const [open, setOpen] = useState(true);  /* useState returns [value, setter]. `open` is the state and `setOpen` updates it. */
    const [ active, setActive] = useState("Overview"); /* the string inside is called the inital value. the value on the very first render only. On every other render it gets ignored  */
                /* different classes and meaning shrik-0: as the child of the outer flex container row this element would usally be able to be compressed but this makes it to where it cannot be 
                    flex: this makes the aside its self a flex contaienr  with flex and flex-col: this makes the children in the flex container a column. bg-
                    overviewhidden: this mean that when the sidebar is closed, the overview content is hidden */
     return (
        /* the outer flex container row  */
       <div className="flex h-screen bg-white font-roboto-mono text-black">
         <aside className={` ${open ? "w-64" : "w-16"} shrink-0 overflow-hidden border-r bg-slate-50 border-slate-200  duration-300 flex flex-col`}> 
            {/* Rail header. Shrink-0 so it never gets compressed by the scrolling nav below it*/}
            <div className="flex h-14 shrink-0 items-center gap-2 px-3"> 
                <button onClick={() => setOpen()} /* button using => does declare a function its called a arrow function */
                className=""> 

                </button>
            </div>


         </aside>
         
       </div>
    )
}