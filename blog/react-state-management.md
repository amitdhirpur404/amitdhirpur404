# Managing State in React: Context API vs Redux

Managing state effectively is crucial when building scalable and performant React applications.

## ✅ What is State?

State refers to data that changes over time within a component or across multiple components.

## ✅ Context API

Use the Context API when:
- You need to pass data through multiple components.
- Your app is small to medium-sized.

Example:
```javascript
const ThemeContext = React.createContext();

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}
