const React = (() => {
    let value;
    let currentComponent = null;
    return {
      render(Component) {
        comp = Component();
        comp.render();
        currentComponent = Component;
        return comp;
      },
      setState(cb) {
        //value값을 다시 지정하고
        //this.render를 호출해야 한다.
        value = cb(value);
        currentComponent().render();
      },
      useState(_initVal) {
        //value가 없으면 initVal을 value로 셋팅
        //value 와 setState 메서드를 배열로 묶어서 반환
        value = value || _initVal;
        return [value, this.setState];
      },
    };
  })();
  
  function MyComponent() {
    const [foo, setFoo] = React.useState(10);
    return {
      render() {
        console.log(`foo value is ${foo}`);
      },
      fireEvent() {
        setFoo((foo) => foo + 1);
      },
    };
  }
  
  //아래처럼 4번 렌더링이 일어난다고 가정한다.
  const component = React.render(MyComponent); //foo value is 10
  component.fireEvent(); //foo value is 11
  component.fireEvent(); //foo value is 12
  component.fireEvent(); //foo value is 13