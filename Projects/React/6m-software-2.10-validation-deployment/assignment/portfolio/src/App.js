// Break down App into its respective react components and import them from separate files for ease of code maintenance

import './App.css';
import styles from './components/MyComponent.module.css';
import Header from './components/Header.js';
import Description from './components/Description.js';
import Location from './components/Location.js';
import Hobbies from './components/Hobbies.js'
import Contact from './components/Contact.js';

function App() {
  return (
    <div className={styles.body}>

      {/* Header with photo */}
      <div>
        <Header />
      </div>

      {/* Brief description about myself */}
      <div className={styles.bodyText}>
        <Description />
      </div>

      {/* My place of residence */}
      <div className={styles.bodyText}>
        <Location />
      </div>

      {/* My hobbies */}
      <div className={styles.bodyText}>
        <Hobbies />
      </div>

      {/* My contact details */}
      <div className={styles.bodyText}>
        <Contact />
      </div>

    </div>
  );
}

export default App;