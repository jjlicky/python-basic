#if문 활용 2 -변형 if, elif, else문)

score = int(input('점수를 입력하세요(1~100점):'))
if score >= 80:
    grade = 'excellent'
elif 50 <= score <80:
    grade = 'good'
else:
    grade = 'poor'

print('{0}점의 등급은 "{1}"입니다.'.format(score,grade))
