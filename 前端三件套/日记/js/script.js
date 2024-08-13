document.addEventListener('DOMContentLoaded', function () {
    const diaryListElement = document.getElementById('diary-list');
    const diaryContentElement = document.getElementById('diary-content');

    // 读取JSON文件
    fetch('../diaries.json')
        .then(response => response.json())
        .then(data => {
            const diaries = data.diaries;

            // 填充侧边栏
            diaries.forEach((diary, index) => {
                const li = document.createElement('li');
                li.textContent = diary.date;
                li.dataset.index = index; // 添加索引以便后续获取内容
                li.addEventListener('click', function () {
                    displayDiaryContent(index);
                });
                diaryListElement.appendChild(li);
            });

            // 显示第一个日记内容
            if (diaries.length > 0) {
                displayDiaryContent(0);
            }
        })
        .catch(error => console.error('Error loading JSON:', error));

    function displayDiaryContent(index) {
        fetch('../diaries.json')
            .then(response => response.json())
            .then(data => {
                const diary = data.diaries[index];
                diaryContentElement.innerHTML = `<h3>${diary.date}</h3><p>${diary.content}</p>`;
            })
            .catch(error => console.error('Error loading JSON:', error));
    }
});
