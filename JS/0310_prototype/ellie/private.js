class Article {
    static publisher = 'Tami world';
    constructor (num){
        this.num= num;
    }
    static printPublicher() {
        console.log(Article.publisher);
    }
}

const article1 = new Article(1);
console.log(article1.publisher); //undefined
console.log(Article.publisher);