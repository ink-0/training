// import useInput from "./components/useInput";
import InputSample from "./components/InputSample";

function App() {
  // //validator 함수
  // const maxLen = (value) => value.length <= 10;

  // //useInput 실행 및 초기값 지정
  // const name = useInput("Mr.", maxLen);

  //렌더링
  return (
    <div className="App">
      <InputSample />
    </div>
  );
}
export default App;
