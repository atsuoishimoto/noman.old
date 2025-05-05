# ssh-keygen command

Generate, manage, and convert authentication keys for SSH.

## Overview

`ssh-keygen` creates public/private key pairs for SSH authentication. These keys allow secure, password-less login to remote systems. The command can also manage existing keys, including changing passphrases and converting between key formats.

## Options

### **-t type**

Specifies the type of key to create. Common types include rsa, ed25519, dsa, and ecdsa.

```console
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
```

### **-f filename**

Specifies the filename of the key file to create or manage.

```console
$ ssh-keygen -t rsa -f ~/.ssh/my_custom_key
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
```

### **-b bits**

Specifies the number of bits in the key. Higher values provide stronger security but may be slower.

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
```

### **-p**

Changes the passphrase of an existing private key file.

```console
$ ssh-keygen -p -f ~/.ssh/id_rsa
Enter old passphrase: 
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
```

### **-C comment**

Adds a comment to the key, typically used to identify the key's purpose or owner.

```console
$ ssh-keygen -t ed25519 -C "work laptop"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
```

## Usage Examples

### Creating a default RSA key pair

```console
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
```

### Generating a key with custom settings

```console
$ ssh-keygen -t ed25519 -b 256 -f ~/.ssh/github_key -C "github access"
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/github_key
Your public key has been saved in /home/user/.ssh/github_key.pub
```

### Viewing a public key's fingerprint

```console
$ ssh-keygen -lf ~/.ssh/id_rsa.pub
3072 SHA256:abcdef1234567890abcdef1234567890 user@hostname (RSA)
```

## Tips

### Choose the Right Key Type

Ed25519 keys are recommended for most modern systems as they offer strong security with smaller key sizes. RSA keys (minimum 2048 bits) are more widely compatible with older systems.

### Use a Strong Passphrase

Adding a passphrase to your private key provides an extra layer of security. If someone obtains your private key file, they'll still need the passphrase to use it.

### Back Up Your Keys

Store a secure backup of your private keys. If you lose them, you'll lose access to any systems that use those keys for authentication.

### Key Permissions Matter

SSH is sensitive to file permissions. Private keys should have permissions set to 600 (readable and writable only by the owner).

```console
$ chmod 600 ~/.ssh/id_rsa
```

## Frequently Asked Questions

#### Q1. How do I copy my public key to a remote server?
A. Use `ssh-copy-id username@remote-server` to copy and install your key. Alternatively, manually append your public key to the remote server's `~/.ssh/authorized_keys` file.

#### Q2. What's the difference between key types?
A. RSA is widely compatible but requires longer keys. Ed25519 is newer, more secure, and uses shorter keys but may not work with older systems. ECDSA and DSA are less commonly used today.

#### Q3. How do I remove a passphrase from my key?
A. Use `ssh-keygen -p -f ~/.ssh/id_rsa` and enter an empty passphrase when prompted for the new passphrase.

#### Q4. How often should I rotate my SSH keys?
A. Best practice is to rotate keys annually or when there's a security concern, such as a team member leaving or a potential compromise.

## macOS Considerations

On macOS, keys are stored in the same location (`~/.ssh/`), but you may need to add your key to the SSH agent with:

```console
$ ssh-add -K ~/.ssh/id_rsa
```

For macOS Monterey (12) and later, use:

```console
$ ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

## References

https://man.openbsd.org/ssh-keygen.1

## Revisions

- 2025/05/04 First revision