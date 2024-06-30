import me from './image/ME1.png';
import image from './image/mainlogo.png';
import add from './image/add.png';
import logout from './image/logout.png';
import submit from './image/submit.png';
import axios from 'axios';
import './App.css';
import { useState ,  useEffect, useRef} from 'react';

function App() {
  //add state for input and chat log
  const [input, setInput] = useState("");
  const [chatLog, setChatLog] = useState([
    {
      user: "gpt",
      message: "How can I help you today?"
    }
  ]);
  
  function clearChat() {
    setChatLog([]);
  }
  
  function LogOut() {
    
    
    window.location.href = 'https://www.google.com';
    
   
    

  }

  
  const handleUpdateAPI = async () => {
    try {
      const response = await axios.get('https://flask-app-oaovyo3kcq-uc.a.run.app/api/create_vector_db');
      console.log(response.data);
    } catch (error) {
      console.error('Error calling the API:', error);
    }
  };



  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Update chat log
    let chatLogNew = [...chatLog, { user: "me", message: `${input}` }]
    //const newChatLog = [...chatLog, { user: "me", message: input }];
    setChatLog(chatLogNew);
    setInput("");

    try {
      

      // Make POST request to the API
      const response = await axios.post("https://flask-app-oaovyo3kcq-uc.a.run.app/api/ask_question", {
        question: input
      });

      // Handle response
      const data = response.data.answer;
      console.log("res",response)
      setChatLog([...chatLogNew, { user: "gpt", message: `${data}` }])
      console.log(data); // Do something with the response data
      console.log("on the try block ")
    } catch (error) {
      console.log("on the catch block ")
      console.error('Error:', error);
    }
  };

  const chatLogRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [chatLog]);

  const scrollToBottom = () => {
    if (chatLogRef.current) {
      chatLogRef.current.scrollTop = chatLogRef.current.scrollHeight;
    }
  };


  return (
    <div className="App">
      <aside className="sidemenu">
        <div className="title-with-image">
          <img src={image} alt="FinanceGPT" className="title-image" />
          <span className="title-text">PESA BARHAO</span>
        </div>
        <div className="side-menu-button" onClick={clearChat}>

          <div>
            <span className="add">
              <img src={add} alt="Add" />
            </span>
            New Chat
          </div>
        </div>
        <div className='side-menu-button update' onClick={handleUpdateAPI}> 
          <span className='update'>
            Update Stock

          </span>
        </div>
        <div className="side-menu-button logout" onClick={LogOut}>

          <span className="logout">
            <img src={logout} alt="Logo" />
          </span>
          Logout

        </div>
      </aside>
      <section className="chatbox">
        <div className="chat-log" ref={chatLogRef} >
          {chatLog.map((message, index) => (
            <ChatMessage key={index} message={message} />

          ))}



        </div>
        <div className="chat-input-holder">
          <form onSubmit={handleSubmit} className="form-container">

            <input rows="1" value={input}
              onChange={(e) => setInput(e.target.value)}
              className="chat-input-textarea" placeholder="Type your query here">

            </input>
            {input.trim()!=="" && (
            <img
              src={submit}// Replace with the URL of your submit button image
              alt="Submit"
              onClick={handleSubmit} // Call handleSubmit function on click
              className="submit-button"
            />
          )}

          </form>

        </div>

      </section>
      
    </div>
  );
}

const ChatMessage = ({ message }) => {
  return (
    <div className={`chat-message ${message.user === "gpt" && "financegpt"}`}>
      <div className="chat-message-center">
        <div className={`avatar ${message.user === "gpt" && "financegpt"}`}>
          {/* <img src={image}/> */}
          {message.user === "gpt" && <img src={image} alt="Avatar" />}
        <div className={`avatar ${message.user==="me" && "meavatar"}`}>
          {message.user==="me" && <img src={me} alt="Me"/>}
        </div>
          

        </div>
        <div className="message">
          {message.message}
        </div>
      </div>
    </div>

  )
}
export default App;
