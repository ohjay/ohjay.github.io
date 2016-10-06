## Discussion Quiz 5 ##
## Disclaimer: this quiz is ridiculous. ##

import math

class Cipher:
    """General cipher class. Identity encryption and decryption."""
    
    def __init__(self):
        self.plainhist = {} # {plaintext: # times encrypted}
        self.cipherhist = {} # {ciphertext: # times "decrypted"}
        
    def encrypt(self, plaintext):
        assert type(plaintext) == str, 'input must be a string'
        self.plainhist[plaintext] = self.plainhist.get(plaintext, 0) + 1
        if self.plainhist.get(plaintext, 0) > 10:
            print("...you've encrypted this %d times"
                    % self.plainhist[plaintext])
        return plaintext
    
    def decrypt(self, ciphertext):
        assert type(ciphertext) == str, 'input must be a string'
        self.cipherhist[ciphertext] = self.cipherhist.get(ciphertext, 0) + 1
        if self.cipherhist.get(ciphertext, 0) > 10:
            print('dude get a life')
        return ciphertext

class RouteCipher(Cipher):
    """Standard route cipher. For encryption, writes plaintext out
    as characters in a rectangular grid, then reads off elements
    a spiraling inward, clockwise fashion (starting at the top left).
    
    For example, HELLO WORLD would be displayed in a two-row grid as
    
    H L O W R D
    E L   O L _
    
    and would be encrypted as HLOWRD_LO LE.
    """
    def __init__(self, num_rows):
        assert num_rows > 0, 'row count must be positive'
        Cipher.__init__(self)
        self.num_rows = num_rows
    
    def spiral_read(grid):
        """Takes a grid and (spirally) reads it into text."""
        num_rows = len(grid)
        if not num_rows: return ''
        num_cols = len(grid[0])
        if not num_cols: return ''
        
        result = ''.join(grid[0]) # top row, left to right
        for r in range(1, num_rows):
            result += grid[r][num_cols - 1] # right column, top to bottom
        if num_rows > 1:
            for c in reversed(range(0, num_cols - 1)):
                result += grid[num_rows - 1][c] # bottom row, right to left
        if num_cols > 1:
            for r in reversed(range(1, num_rows - 1)):
                result += grid[r][0] # left column, bottom to top
        subgrid = [grid[r][1:(num_cols - 1)] for r in range(1, num_rows - 1)]
        return result + RouteCipher.spiral_read(subgrid) # is RouteCipher. necessary?
    
    def spiral_grid(text, num_rows):
        """Takes text and (spirally) reads it into a grid."""
        if num_rows <= 0: return [[]]
        num_cols = math.ceil(len(text) / num_rows)
        if num_cols <= 0: return [[]]
        grid = RouteCipher.empty_grid(num_rows, num_cols)
        
        r, c = 0, 0
        for c in range(num_cols):
            grid[0][c] = text[c] # the top row of the grid
        for r in range(1, num_rows):
            grid[r][num_cols - 1] = text[c + r] # right column
        text = text[(c + r + 1):]
        if num_rows > 1:
            for c in range(0, num_cols - 1):
                grid[num_rows - 1][num_cols - c - 2] = text[c] # bottom row
            text = text[c:]
        if num_cols > 1:
            for r in range(1, num_rows - 1):
                grid[num_rows - r - 1][0] = text[r] # left column
        subgrid = RouteCipher.spiral_grid(text[(r + 1):], num_rows - 2)
        for r in range(num_rows - 2):
            for c in range(len(subgrid[0])):
                grid[1 + r][1 + c] = subgrid[r][c]
        return grid
    
    def empty_grid(num_rows, num_cols):
        return [['_' for _ in range(num_cols)] for _ in range(num_rows)]
    
    def encrypt(self, plaintext):
        Cipher.encrypt(self, plaintext) # make sure assertions happen
        num_cols = math.ceil(len(plaintext) / self.num_rows)
        grid = RouteCipher.empty_grid(self.num_rows, num_cols)
        r, c = 0, 0
        for char in plaintext:
            grid[r][c] = char
            r = (r + 1) % self.num_rows
            if r == 0: c += 1
        return RouteCipher.spiral_read(grid) # why not self.?
    
    def decrypt(self, ciphertext):
        Cipher.decrypt(self, ciphertext)
        grid = RouteCipher.spiral_grid(ciphertext, self.num_rows)
        
        # Read... in the order by which the grid was originally constructed
        plaintext = ''
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                plaintext += grid[r][c]
        return plaintext.strip('_')

## Extensions for the enthusiastic. ##

class PaddedRouteCipher(RouteCipher):
    """Route cipher w/ fixed beginning and ending padding text (before encryption)."""

class InterleavedRouteCipher(RouteCipher):
    """Route cipher w/ a fixed string inserted after every N input chars (before encryption)."""
