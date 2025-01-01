// React component for hobbies

import styles from './MyComponent.module.css';

function Hobbies() {
    return (
        <>
            <h3>Hobbies</h3>
            <hr />
            <div className={styles.listContainer}>
                <ul className={styles.verticalList}>
                    <li>swimming</li>
                    <li>playing guitar</li>
                    <li>plastic modelling</li>
                </ul>
            <br />
            </div>
        </>
    );
}

export default Hobbies;