import { Directory } from './../src/Directory';
import { BinaryFile } from './../src/BinaryFile';

describe('Binary file', () => {
  const rootDir = new Directory(null, 'root');

  test('should be successfully created', () => {
    expect(() => new BinaryFile(rootDir, 'file1')).not.toThrowError();
  });

  describe('default file', () => {
    const bf = new BinaryFile(rootDir, 'file2');

    test('should have a proper default content', () => {
      expect(bf.content).toBe('');
    });

    test('should have a proper parent', () => {
      expect(bf.parent).toBe(rootDir);
    });
  });

  describe('named and filled file', () => {
    const content = 'lorem ipsum dolor sit amet...';
    const filename = 'file3';
    const bf = new BinaryFile(rootDir, filename, content);

    test('should have a proper filename', () => {
      expect(bf.name).toBe(filename);
    });

    test('should have a proper content', () => {
      expect(bf.content).toBe(content);
    });
  });
});
