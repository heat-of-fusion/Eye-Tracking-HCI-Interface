from win32api import GetSystemMetrics

# Dictionary to convert jaums to double-jaum.
double_jaum_dict = {
    'ㄱㄱ': 'ㄲ',
    'ㄱㅅ': 'ㄳ',
    'ㄴㅈ': 'ㄵ',
    'ㄴㅎ': 'ㄶ',
    'ㄷㄷ': 'ㄸ',
    'ㄹㄱ': 'ㄺ',
    'ㄹㅁ': 'ㄻ',
    'ㄹㅂ': 'ㄼ',
    'ㄹㅅ': 'ㄽ',
    'ㄹㅌ': 'ㄾ',
    'ㄹㅍ': 'ㄿ',
    'ㄹㅎ': 'ㅀ',
    'ㅂㅂ': 'ㅃ',
    'ㅂㅅ': 'ㅄ',
    'ㅅㅅ': 'ㅆ',
    'ㅈㅈ': 'ㅉ'
}

# Dictionary to convert moums to double-moum
double_moum_dict = {
    'ㅗㅏ': 'ㅘ',
    'ㅗㅐ': 'ㅙ',
    'ㅗㅣ': 'ㅚ',
    'ㅜㅔ': 'ㅞ',
    'ㅜㅓ': 'ㅝ',
    'ㅜㅣ': 'ㅟ',
    'ㅡㅣ': 'ㅢ',
    'ㅑㅣ': 'ㅒ',
    'ㅣㅕ': 'ㅒ',
    'ㅕㅣ': 'ㅖ',
    'ㅏㅣ': 'ㅐ',
    'ㅣㅓ': 'ㅐ',
    'ㅓㅣ': 'ㅔ',

}

class GhostCursor():
    '''
    This class function as a virtual cursor, but not used in current versionl.
    '''
    def __init__(self, init_Y, init_X):
        self.y = init_Y
        self.x = init_X

        self.res_Y = GetSystemMetrics(1)
        self.res_X = GetSystemMetrics(0)

        return

    def move(self, dy, dx):
        '''
        Move virtual cursor
        :param dy: Distance to move the cursor along y-axis.
        :param dx: Distance to move the cursor along x-axis.
        :return: None
        '''
        self.y = min(self.res_Y, max(0, self.y + dy))
        self.x = min(self.res_X, max(0, self.x + dx))

        return

def blinkdecorator(func):
    '''
    Decorator to make the button blink after the functioning.
    :param func: function to apply decorator.
    :return: None
    '''
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.blink()

        return

    return wrapper