const Parser = require('rss-parser')
const parser = new Parser();

// RSS 피드 파싱하기
const init = async () => {
    const feed = await parser.parseURL('https://ballboydev.github.io/rss');

    console.log(feed.title); // 블로그 제목
    feed.items.forEach(item => {
        console.log(item.title); // 각 글의 제목
        console.log(item.link);  // 각 글의 링크
    });
}


init()